# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preOrder(root, depth):
            if not root:
                return
            else:
                vals.append(str(root.val) + depth * '-')
                preOrder(root.left, depth + 1)
                preOrder(root.right, depth + 1)
        preOrder(root, 1)
        return ' '.join(vals)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        vals = data
        def build(depth):
            if vals:
                val = vals.pop(0)
                curr_depth = val.count('-')
                if curr_depth == depth:
                    vals.insert(0, val)
                    return
                node_val = val.replace(curr_depth * '-', '')
                node_val = int(node_val)
                # if curr_depth 
                node = TreeNode(node_val)
                node.left = build(depth + 1)
                node.right = build(depth + 1)
                return node
        return build(1)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))