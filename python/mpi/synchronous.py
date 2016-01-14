def syn_master(batch_buffer,k,n_core,eta,alpha):
    new_eta = eta

    processes = []
    q = Queue()

    for i in xrange(n_core):
        d,eta,etaSum = batch_buffer[i]
        prc = Process(target = syn_worker, args = (d,eta,etaSum,alpha,q))
        processes.append(prc)
        prc.start()
        
    for i in xrange(n_core):
        delta_eta = q.get()
        _mea.add_eta(new_eta,delta_eta)
        
    for prc in processes:
        prc.join()
        
    return new_eta

def syn_worker(d,eta,etaSum,alpha,q):
    delta_eta =  _mworker.lda_worker(d,eta,etaSum,alpha)
    q.put(delta_eta)