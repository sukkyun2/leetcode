class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        def filter_addr(addr):
            if addr.find('+') != -1:
                addr = addr[:addr.find('+')]
            addr = addr.replace('.','')
            return addr
        
        for email in emails:
            e = email.split('@')
            s.add(filter_addr(e[0]) + '@' + e[1])
        print(s)
        return len(s)
        