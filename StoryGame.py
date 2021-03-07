# Tree class
class StoryGame:
    # Constructor
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.story = []

    # Add method
    # Adding story piece to the root/parent node
    def add_story(self, story):
        self.story.append(story)

    # Print each story till end
    # Player has choices to go through the story lines
    def print_story(self):
        story_i = self
        print(story_i.story_piece)

        while story_i.story:
            print()
            choice = int(input('Enter 1 or 2 to continue: ')) - 1
            if choice not in [0, 1]:
                choice = int(input('Enter 1 or 2 to continue: ')) - 1
            chosen = story_i.story[choice]
            print(chosen.story_piece)

            story_i = chosen


# Root story and children instances
# Every instance has a story that you can chose while you play
# With different story lines and endings
game = StoryGame('Hey Adventurer! You have entered a cave,\n'
                 'You can go right or left what do you chose?\n'
                 '- Go right: 1\n'
                 '- Go left: 2 ')
game_a = StoryGame('Ohh I think it is cold here I should find something to warm up...\n'
                   'You see a light there... what will you do?\n'
                   '- Find out what is it: 1\n'
                   '- Keep searching for something to warm up: 2')
game_b = StoryGame('Dark place, nothing to see here but I should keep going...\n'
                   'Something roars in front of you, what is your next step?\n'
                   '- Run toward the thing: 1\n'
                   '- Wait until there is silence: 2')
game_c = StoryGame('Hmm it seems like the light has gone...\n'
                   '...wow more tunnels\n'
                   '- Turn left: 1'
                   '- Go forward: 2')
game_d = StoryGame('Walking for a while...\n'
                   'You have found a lighter, now you see better in the dark\n'
                   '...and you began to warm up, will you walk further or rest a bit?\n'
                   '- Walk: 1\n'
                   '- Rest: 2')
game_e = StoryGame('You begin to run but with fear in your mind...\n'
                   'After a couple of minutes of running you reach a small lake.\n'
                   'You wonder how is it possible, a lake in a cave?\n'
                   '- Jump to it: 1\n'
                   '- Walk along it till find another way: 2')
game_f = StoryGame('After a couple of hours you still have not found a torch...\n'
                   'or just something to warm up and you feel hopeless.\n'
                   '- Encourage yourself to keep going: 1\n'
                   '- Go back to the entrance and leave: 2')
game_g = StoryGame('Oh nooo....\n'
                   'You have been eaten by a grizzly bear!')
game_h = StoryGame('While you were walking something or someone has knocked you out...\n'
                   'Unfortunately you died.')
game_i = StoryGame('Strange noises...\n'
                   'Suddenly a monster appeared...and killed you.')
game_k = StoryGame('After a big rest an ogre has found you...\n'
                   'It came out from nowhere and killed you.')
game_l = StoryGame('The lake was so cold that you have frozen to death.')
game_m = StoryGame('Some ugly goblins appeared...\n'
                   'And attacked you...\n'
                   'You died')
game_n = StoryGame('Scary tunnels...\n'
                   'Something you see hear that slowly approaching you...'
                   'Ah it is just a...Baby goblin!'
                   'Noo it killed you.')
game_o = StoryGame('You are a very lucky person...\n'
                   'No one has survived the way back to the entrance...')

# Connecting each story to other
game.add_story(game_a)
game.add_story(game_b)
# A choice
game_a.add_story(game_c)
game_a.add_story(game_d)
# B choice
game_b.add_story(game_e)
game_b.add_story(game_f)
# C choice
game_c.add_story(game_g)
game_c.add_story(game_h)
# D choice
game_d.add_story(game_i)
game_d.add_story(game_k)
# E choice
game_e.add_story(game_l)
game_e.add_story(game_m)
# F choice
game_f.add_story(game_n)
game_f.add_story(game_o)

game.print_story()
