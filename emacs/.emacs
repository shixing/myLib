(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ecb-options-version "2.40"))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(require 'ido)
(ido-mode t)

;; CEDET

(load-file "/Users/xingshi/.emacs.d/cedet-1.1/common/cedet.el")
(global-ede-mode 1)                      ; Enable the Project management system
(semantic-load-enable-minimum-features)
(semantic-load-enable-code-helpers)      ; Enable prototype help and smart completion 
(global-srecode-minor-mode 1)   

;;ECB
(add-to-list 'load-path "/Users/xingshi/.emacs.d/ecb-2.40")
(load-file "/Users/xingshi/.emacs.d/ecb-2.40/ecb.el")
(require 'ecb-autoloads)
(setq stack-trace-on-error t)
(setq ecb-tip-of-the-day nil)

;;auto-complete
(add-to-list 'load-path "~/.emacs.d/auto-complete-1.3.1/")
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/.emacs.d/auto-complete-1.3.1/ac-dict/")
(ac-config-default)

;;ac-python.el
;;(add to list 'load-path "~/.emacs.d/auto-complete-1.3.1/ac-python.el")
;;(require 'ac-python)

;;set color
(set-background-color "black")
(set-foreground-color "yellow")
(set-cursor-color "purple")

;;change keymap
(global-set-key [?\S- ] 'set-mark-command)

(put 'upcase-region 'disabled nil)

;; for tramp
(add-to-list 'load-path "~/emacs.d/tramp-2.2.6/lisp/")
(require 'tramp)
(add-to-list 'Info-default-directory-list "~/emacs.d/tramp-2.2.6/info/")

;; CEDET

;; Enabling Semantic (code-parsing, smart completion) features
;; Select one of the following:
;;(semantic-load-enable-minimum-features)
;;(semantic-load-enable-code-helpers)
;;(semantic-load-enable-gaudy-code-helpers)
(semantic-load-enable-excessive-code-helpers)
;;(semantic-load-enable-semantic-debugging-helpers)
 
;;;; 使函数体能够折叠或展开
;; Enable source code folding
(global-semantic-tag-folding-mode 1)
 
;; Key bindings
(defun my-cedet-hook ()
  (local-set-key (kbd "C-c ?") 'semantic-ia-complete-symbol-menu)
  (local-set-key (kbd "C-c d") 'semantic-ia-fast-jump)
  (local-set-key (kbd "C-c r") 'semantic-symref-symbol)
  (local-set-key (kbd "C-c R") 'semantic-symref))
;;(add-hook 'c-mode-hook 'my-cedet-hook)
(add-hook 'python-mode-hook 'my-cedet-hook)
 
;;;; 当输入"."或">"时，在另一个窗口中列出结构体或类的成员
(defun my-c-mode-cedet-hook ()
  (local-set-key "." 'semantic-complete-self-insert)
  (local-set-key ">" 'semantic-complete-self-insert))
;;(add-hook 'c-mode-hook 'my-c-mode-cedet-hook)
;;(add-hook 'python-mode-hook 'my-c-mode-cedet-hook)

(require 'semantic-tag-folding)
(defun folding-hook ()
  (local-set-key (kbd "C-c <left>") 'semantic-tag-folding-fold-block)
  (local-set-key (kbd "C-c <right>") 'semantic-tag-folding-show-block)
)
(add-hook 'python-mode-hook 'folding-hook)
(put 'scroll-left 'disabled nil)

;;;; For julia mode

(load-file "/Users/xingshi/.emacs.d/julia-mode.el")
