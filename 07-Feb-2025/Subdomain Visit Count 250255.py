# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ans = []

        top = {}
        middle = {}
        lowest = {}

        for string in cpdomains:
            count, domains = string.split()
            count = int(count)

            domains = domains.split(".")

            d3 = domains[-1]
            d2 = ".".join(domains[-2:])

            if len(domains) == 3:
                d1 = ".".join(domains[:])
                lowest[d1] = lowest.get(d1,0) + count

            top[d3] = top.get(d3,0) + count
            middle[d2] = middle.get(d2, 0) + count  
            
        for domain in top:
            ans.append(f"{str(top[domain])} {domain}")

        for domain in middle:
            ans.append(f"{str(middle[domain])} {domain}")

        for domain in lowest:
            ans.append(f"{str(lowest[domain])} {domain}")
        
        return ans
            

        