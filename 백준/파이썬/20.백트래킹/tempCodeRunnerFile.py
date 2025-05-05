    visited[i] = True
                path.append(i)
                backtracking()
                path.pop()
                visited[i] = False