import hashlib
import merkle_tree_stream
import codecs

def _leaf(node, roots=None):
    print("This is the digest of the node: ")
    print(hashlib.sha256(node.data).digest())
    return hashlib.sha256(node.data).digest()


def _parent(first, second):
    sha256 = hashlib.sha256()
    sha256.update(first.data)
    sha256.update(second.data)
    print("This is the digest of the parent: ")
    print(sha256.digest())
    return sha256.digest()

merkle = merkle_tree_stream.MerkleTreeGenerator(leaf=_leaf, parent=_parent)


merkle.write(b"a")
merkle.write(b"b")
merkle.write(b"b")
merkle.write(b"b")

#assert len(merkle) == 2 + 1


