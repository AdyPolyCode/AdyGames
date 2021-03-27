class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_next_node(self, new):
        self.next_node = new

    def get_next_node(self):
        return self.next_node


class Stack:
    def __init__(self, limit=None):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def push(self, value):
        if self.has_space():
            new = Node(value)
            new.set_next_node(self.top_item)
            self.top_item = new

            self.size += 1
        else:
            raise Exception(' - This Stack is full -')

    def pop(self):
        if not self.is_empty():
            to_remove = self.top_item
            self.top_item = to_remove.get_next_node()

            self.size -= 1
            return to_remove.value
        else:
            raise Exception('- This Stack is empty -')

    def peek(self):
        if not self.is_empty():
            return self.top_item.value

    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

    def print_stack(self):
        stack = []
        top = self.top_item
        while top:
            stack.insert(0, top.get_value())
            top = top.get_next_node()
        return stack


# Asking the user for disk number
user = int(input('With how many plates do you want to play?: '))
while user < 2:
    user = int(input('With how many plates do you want to play?: '))


winStack = []
mainStack = []  # Helper stack to display information easier

leftStack = Stack(user)
midStack = Stack(user)
rightStack = Stack(user)

for i in range(user, 0, -1):  # Push every disk to the left most stack
    leftStack.push(i)
for i in range(user):
    winStack.append('*')

mainStack.append(leftStack)
mainStack.append(midStack)
mainStack.append(rightStack)


def display_stacks():
    print(leftStack.print_stack())
    print(midStack.print_stack())
    print(rightStack.print_stack())


def user_choice():
    to_stacks = []
    from_stacks = []
    for stack in mainStack:
        if not stack.is_empty():
            from_stacks.append(mainStack.index(stack) + 1)
        if stack.has_space():
            to_stacks.append(mainStack.index(stack) + 1)

    # display the stacks that can be chose from + user choice
    print(f'Currently you can push the disk from {from_stacks}.')
    from_choice = int(input(f'From where to push: '))

    while from_choice not in range(1, 4) or from_choice not in from_stacks:
        from_choice = int(input(f'From where to push: '))

    print()
    # display the stacks that can be pushed to + user choice
    print(f'Currently you can push the disk to {to_stacks}.')
    to_choice = int(input(f'Where to push: '))

    while to_choice not in range(1, 4) or to_choice not in to_stacks:
        to_choice = int(input(f'Where to push: '))

    print()
    disk_to_push = mainStack[from_choice - 1].peek()
    stack_to_push = mainStack[to_choice - 1].peek()
    stack_from_index = from_choice - 1
    stack_to_push_index = to_choice - 1

    return disk_to_push, stack_to_push, stack_to_push_index, stack_from_index


def play_again():
    again = input('Do you want to play again? (y/n): ').upper()
    while again not in ['Y', 'N']:
        again = input('Do you want to play again? (y/n): ').upper()
    return again


def main():
    print('Welcome to TowerOfHanoi! Let\'s play.')
    print()
    game_on = True
    while game_on:
        display_stacks()
        disk_val, stack_last_val, stack_to_index, stack_from_index = user_choice()
        while stack_last_val is not None and disk_val > stack_last_val:
            print(f'You cannot push {disk_val} to this {mainStack[stack_to_index].print_stack()} stack.')
            disk_val, stack_last_val, stack_to_index, stack_from_index = user_choice()
        else:
            mainStack[stack_from_index].pop()
            mainStack[stack_to_index].push(disk_val)

        if len(mainStack[1].print_stack()) == len(winStack):
            print('You won!')
            replay = play_again()
            if replay == 'Y':
                print()
                main()
            else:
                print('Bye')
                break
        if len(mainStack[2].print_stack()) == len(winStack):
            print('You won!')
            replay = play_again()
            if replay == 'Y':
                print()
                main()
            else:
                print('Bye')
                break


main()