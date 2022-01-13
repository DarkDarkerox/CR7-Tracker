import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import sqlite3


query = """
    SELECT followers, time FROM cristiano_data
"""

with sqlite3.connect('instadb.db') as conn:
    cursor = conn.cursor()
    result = cursor.execute(query, ())
    conn.commit()

followers =[]
time = []

for data in result:
    followers.append(data[0])
    time.append(data[1])

fig, ax = plt.subplots()
ax.plot(time[:], followers[:])
loc = plticker.MultipleLocator(base=50.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
plt.show()