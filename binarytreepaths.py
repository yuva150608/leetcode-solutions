class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, res):
            if not node:
                return
            
            # Append current node to the path
            path += str(node.val)
            
            # If it's a leaf, save the full path
            if not node.left and not node.right:
                res.append(path)
            else:
                # If not a leaf, add the arrow and continue to children
                path += "->"
                dfs(node.left, path, res)
                dfs(node.right, path, res)
        
        result = []
        dfs(root, "", result)
        return result
