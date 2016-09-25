

def is_tree(tree)
    is type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branches(tree)):
            return False
    return Ture

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]


def tree(root, branches=[ ]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)
    
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def branches(tree):
    return tree[1:]