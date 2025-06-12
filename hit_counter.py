class HitCounter:

    def __init__(self):
        self.hit_count = defaultdict(int)
        # list will tell me 
        self.list_timestamps = []

    def hit(self, timestamp: int) -> None:
        hc = self.hit_count
        lst_ts = self.list_timestamps
        if timestamp in hc:
            hc[timestamp]+=1
        else:
            hc[timestamp]+=1
            lst_ts.append(timestamp)
        # timestamp [ 100, 200 , 250 ]
        # check if the timestamp exists, then increment the count
        # if not add at 2 places, dict and list 
        

    def getHits(self, timestamp: int) -> int:
        hc = self.hit_count
        lst_ts = self.list_timestamps
        cnt_hits = 0
        # val = 350 -300 = 50 
        last_ts= timestamp - 300+1
        pos = bisect_left(lst_ts, last_ts)
        for i in range(pos,len(lst_ts)):
            ts = lst_ts[i]
            cnt_hits+=hc[ts]
        return cnt_hits



        # get the position in the list where this would be 
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)