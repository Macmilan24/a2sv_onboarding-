# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, wv: List[List[str]], friends: List[List[int]], idd: int, level: int) -> List[str]:
        n = len(wv)
        visited = set([idd])
        queue = deque([(idd, 0)])
        friends_found = []
            
        while queue:
            idd, dist = queue.popleft()
            
            if dist > level:
                break
            
            if dist == level:
                friends_found.append(idd)
            
            for fri in friends[idd]:
                if fri not in visited:
                    visited.add(fri)
                    queue.append((fri, dist + 1))
        
        video_freq = defaultdict(int)
        for idd in friends_found:
            for video in wv[idd]:
                video_freq[video] += 1
        
        res = sorted(video_freq.keys(), key=lambda x: (video_freq[x], x))
        
        return res
