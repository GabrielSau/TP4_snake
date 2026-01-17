import MovingEntity

class Snake(MovingEntity):
    def __init__ ( self , x , y):
        super () . __init__ ()
        self . _body = [(x , y) ]
        self . _grow_pending = 0

    def update(self):
        super ().update()
        