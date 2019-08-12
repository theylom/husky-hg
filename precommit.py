import re
import mercurial, sys, os
def precommit_hook(ui, repo, **kwargs):
    try:
        # keep a copy of repo.commitctx
        commitctx = repo.commitctx

        def updatectx(ctx, error):

            # check if `ctx.branch()` matches ...
            if ctx._text != None and ctx._text != "":
                print ctx._text
                #commitMsg = input("Enter commit message to add to '%s': "%ctx.branch())
                # update commit text
                ctx._text = ("[#%s] " % ctx.branch()) + ctx._text
                print ctx._text

            # call original
            return commitctx(ctx, error)

        # monkeypatch the commit method
        repo.commitctx = updatectx
    except e:
        print e