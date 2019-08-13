import re
import mercurial, sys, os
def precommit_hook(ui, repo, **kwargs):
    try:
        # keep a copy of repo.commitctx
        commitctx = repo.commitctx

        def updatectx(ctx, error):

            # check if `ctx.branch()` matches ...
            if ctx._text != None and ctx._text != "":
                if re.match(r".*\[#[A-Z]+-[0-9]+\].*", ctx._text) is None:
                    ctx._text = ("[#%s] " % ctx.branch()) + ctx._text
                    print "Updated commit message: " + ctx._text

            # call original
            return commitctx(ctx, error)

        # monkeypatch the commit method
        repo.commitctx = updatectx
    except e:
        print e