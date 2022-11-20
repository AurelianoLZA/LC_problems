import collections
import functools
import math
from typing import List
from typing import Optional

'''

'''


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def change(email: str):
            local = email.split("@")[0]
            domain = email.split("@")[1]
            val = []
            for ch in local:
                if ch == ".":
                    continue
                if ch == "+":
                    break
                else:
                    val.append(ch)
            return "".join(val) +"@"  + domain
        res = []
        for email in emails:
            new_email = change(email)
            if not res:
                res.append(new_email)
            else:
                if new_email not in res:
                    res.append(new_email)
        return len(res)






sol = Solution()
res = sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
res = sol.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
print(res)
