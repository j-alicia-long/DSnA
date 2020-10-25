# Mastercard interview 10/23

# Candidate class
class Candidate:

  def __init__(self, name, speciality, school):
    self.name = name
    self.speciality = speciality
    self.school = school
    self.schedule = {}


def getIntervieweeSchedules(input):

  candidate_info = []

  names = input[0].split(",")[1:]
  speciality = input[1].split(",")[1:]
  schools = input[2].split(",")[1:]

  for i in range(len(names)):
    candidate_info.append(
      {
        "name": names[i],
        "speciality": speciality[i],
        "school": schools[i],
        "schedule": []
      }
    )

  schedule_info = input[3:]

  for row in schedule_info:
    events = row.split(",")
    timeslot = events[0]
    candidate_events = events[1:]

    for i in range(len(names)):
      candidate_info[i]["schedule"].append((timeslot, candidate_events[i]))


  # turn array into dict
  candidate_list = {}

  for candidate in candidate_info:
    candidate_list[candidate["name"]] = candidate

  return candidate_list


def getInterviewerSchedules():
  pass



input = [
",Anthony Bruce,Scott Setrakian,Patrick O'Reilly,Cathy Baker,Andrew Fedorchek",

",Front End,SE,SE,SE Intern,UX",

",CMU,CMU,Penn,UMD,CMU",

"8:30 - 9:00,Arrival / Breakfast,Arrival / Breakfast,Arrival / Breakfast,Arrival / Breakfast,Arrival / Breakfast",

"9:00 - 9:45,Presentation w/ Helen Lovejoy,Presentation w/ Helen Lovejoy,Presentation w/ Helen Lovejoy,Presentation w/ Helen Lovejoy,Presentation w/ Helen Lovejoy",
]

print(getIntervieweeSchedules(input))






# A large group of people plan to ascend a mountain,
# but they will need to split up into groups of 3.
# Each group will need: a navigator to guide them, a survivalist to keep them alive,
# and a brute to carry the equipment.
# Each person has an ability to perform each of the roles described by an
#  integer ranging from 0 to 100. Given a list of people and their skills,
#  we are going to organize them into N teams such that we maximize the minimum team score.


# I am going to give you an algorithm called GeneratePermutations(int n)
#  which will take an integer as an input and return all of the permutations as a List<List<int>>. For example:

# GeneratePermutations(6)
# { 0, 1, 2, 3, 4, 5 }
# { 0, 1, 2, 3, 5, 4 }
# { 0, 1, 2, 4, 3, 5 }
# { 0, 1, 2, 4, 5, 3 }
# ...

{
  "name": ""
  "nav": 0
  "survival": 0
  "brute": 0
}

# List of people's stats
[
[0, 0, 0], # nav, survival, brute
[0, 0, 0],
[0, 0, 0]
]

def GetBestMinTeamScore(inputPersons):

  N = len(inputPersons)
  # Split possible combo into groups
  combos = GeneratePermutations(N):

  max_lowest_score = 0

  lowest_team_score = float("inf")

  for order in range(combos):
    # Find local max for all teams
    for i in range(N/3):
      # Team
      max_score = 0
      team_role_combo = GeneratePermutations(3)
      for team_combo in team_role_combo:
        team_score = 0
        for i in range(3):
          team_score += inputPersons[team_combo[i]][i]

        max_score = max(team_score, max_score)

      lowest_team_score = min(lowest_team_score, max_score)

    max_lowest_score = max(lowest_team_score, max_lowest_score)
