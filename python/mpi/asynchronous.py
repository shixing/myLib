import logging
from multiprocessing import Lock, Pool
from sxsda.locked import LockedSum, LockedEta

# some action
def callback(delta_eta,lockedEta,nActPro,nBatch,var_path,nthread,thread_batch,old_doc_seen):
    lockedEta.add_eta(delta_eta)
    nActPro.add_value(-1)
    nBatch.add_value(1)
        
def asyn_worker():
    pass

def asyn_framework():
    pool = Pool(processes  = nthread)
    nActPro = LockedSum(0,Lock())
    nBatch = LockedSum(0,Lock())
    results = []
    for doc in corpus:
        
        
        if doc_id % thread_batch == thread_batch - 1:   # accumulate one batch

            while True: # check for active processes amount
                if nActPro.get_value() < nthread:
                    break
                
            cb = lambda x: callback(x,lockedEta,nActPro,nBatch,var_path,nthread,thread_batch,old_doc_seen)
            result = pool.apply_async(asyn_workder,(doc_buffer,eta_temp,etaSum,alpha),callback = cb)
            results.append(result)
            nActPro.add_value(1)
            
            # clear buffer
            doc_buffer = []
            voc_temp = set()
            batch_id += 1
            
            doc_id += 1

    # some remain doc may not be processed

    if len(doc_buffer) > 0:

        while True: # check for active processes amount
            if nActPro.get_value() < nthread:
                break
                
        cb = lambda x: callback(x,lockedEta,nActPro,nBatch,var_path,nthread,thread_batch,old_doc_seen)
        result = pool.apply_async(asyn_workder,(doc_buffer,eta_temp,etaSum,alpha),callback = cb)
        results.append(result)
        nActPro.add_value(1)
        batch_id += 1

    for r in results:
        r.wait()

    if nBatch.get_value() % nthread != 0:
        nBatch_value = nBatch.get_value()
        fn = 'eta.{}.pickle'.format(nBatch_value/nthread)
        path = os.path.join(var_path,fn)
        lockedEta.write_eta(path)
        
    return lockedEta.eta
