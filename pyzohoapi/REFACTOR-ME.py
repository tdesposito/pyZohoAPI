    # TODO: What to we do with this?
    def updateAspect(self, aspect, aspect_id, aspect_key, newData):
        if self.loaded:
            url = self._build_url(extraComponents=[aspect, aspect_id])
            rsp = requests.put(url, json=newData)
            if rsp.ok:
                rdata = rsp.json()
                rkey = [k for k in rdata.keys() if k not in ['code', 'message']][0]
                self._data[aspect_key] = rdata[rkey]
                return True
        return False
