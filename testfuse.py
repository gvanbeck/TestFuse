#!/usr/bin/env python


from __future__ import with_statement

import os
import sys
import errno

from fusepy.fuse import FUSE, FuseOSError, Operations


class Passthrough(Operations):
    def __init__(self, root):
        self.root = root

    # Helpers
    # https://www.stavros.io/posts/python-fuse-filesystem/
    # =======

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    #FileSystem methods
    def getattr(self, path, fh=None):
        return super(Passthrough, self).getattr(path, fh)

    def chown(self, path, uid, gid):
        full_path = self._full_path(path)
        return os.chown(full_path, uid, gid)

    def chmod(self, path, mode):
        full_path = self._full_path(path)
        return os.chmod(full_path, mode)

    def access(self, path, amode):
        full_path = self._full_path(path)
        if not os.access(full_path, amode):
            raise FuseOSError(errno.EACCES)

    def readdir(self, path, fh):
        return super(Passthrough, self).readdir(path, fh)



    def fsync(self, path, datasync, fh):
        return super(Passthrough, self).fsync(path, datasync, fh)

    def release(self, path, fh):
        return super(Passthrough, self).release(path, fh)

    def flush(self, path, fh):
        return super(Passthrough, self).flush(path, fh)

    def truncate(self, path, length, fh=None):
        return super(Passthrough, self).truncate(path, length, fh)

    def write(self, path, data, offset, fh):
        return super(Passthrough, self).write(path, data, offset, fh)

    def read(self, path, size, offset, fh):
        return super(Passthrough, self).read(path, size, offset, fh)

    def create(self, path, mode, fi=None):
        return super(Passthrough, self).create(path, mode, fi)

    def open(self, path, flags):
        return super(Passthrough, self).open(path, flags)

    def utimens(self, path, times=None):
        return super(Passthrough, self).utimens(path, times)

    def link(self, target, source):
        return super(Passthrough, self).link(target, source)

    def rename(self, old, new):
        return super(Passthrough, self).rename(old, new)

    def symlink(self, target, source):
        return super(Passthrough, self).symlink(target, source)

    def unlink(self, path):
        return super(Passthrough, self).unlink(path)

    def rmdir(self, path):
        return super(Passthrough, self).rmdir(path)

    def mkdir(self, path, mode):
        return super(Passthrough, self).mkdir(path, mode)

    def mknod(self, path, mode, dev):
        return super(Passthrough, self).mknod(path, mode, dev)

    def readlink(self, path):
        return super(Passthrough, self).readlink(path)


if __name__ == '__main__':
    # FUSE(Passthrough(sys.argv[2], sys.argv[1], nothreads=True, foreground=True))
    print 'Hello World'
