from project.band_members.musician import Musician


class Drummer(Musician):

    VALID_SKILLS = [
        "play the drums with drumsticks",
        "play the drums with drum brushes",
        "read sheet music"
]

    def learn_new_skill(self, new_skill: str):
        '''Each musician can learn a new skill (one at a time):
                    •	If the new skill is not in the skills available for the type of musician,
                    raise a ValueError with the message "{new skill} is not a needed skill!"
                    •	If the new skill is already learned,
                    raise an Exception with the message "{new skill} is already learned!"
                    •	If everything is okay,
                    return the following message: "{musician name} learned to {new skill}."
'''
        if new_skill not in Drummer.VALID_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."