class Mobile:
    def __init__(self, brand , model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def upgrade_storage(self,size):
        self.storage += size

    def print_current_specs(self):
        print("Current specs : ","Brand : ",self.brand ,"Model : ", self.model ,"Storage : ", self.storage)

mobile = Mobile("Samsung","S25plus",256)
mobile.upgrade_storage(256)
mobile.print_current_specs()