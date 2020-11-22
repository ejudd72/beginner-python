from Chef import Chef

# putting the inherited class in the parenthesis
class ChineseChef(Chef):
    # this overwrites what the chef does
    def make_special_dish(self):
        print("The chef makes lemon chicken")
    # this adds a new piece of functionality
    def make_fried_rice(self):
        print("The chef makes fried rice")