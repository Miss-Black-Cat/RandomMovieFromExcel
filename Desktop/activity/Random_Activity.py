import pandas as pd
import random
activityTable = pd.read_excel(r'/Users/mac/Desktop/movies.xlsx')
randomActivity=random.randint(1,len(activityTable))
activities=pd.DataFrame(activityTable).to_numpy()
print(activities[randomActivity,0])
