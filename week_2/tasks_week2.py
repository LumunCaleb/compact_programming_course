#After learing about functions
#I will implement my solutions using functions in this week

from ast import List
from datetime import date

# Task 1
#To get a list sorted in increasing order by the last element in the list
def sort_tuple_last_element(items):
	return sorted(items, key=lambda item: item[-1])


# Task 2
#To return the sum and average of the digits that appear in the string, ignoring all other characters.
def sum_and_average_digits(s1):
	digits = [int(character) for character in s1 if character.isdigit()]
	total = sum(digits)
	average = total / len(digits) if digits else 0
	return total, average


# Task 3
#To sort a list of dictionaries using lambda
def sort_dictionaries_by_color(items):
	return sorted(items, key=lambda item: item["color"])


# Task 4
#To convert a list of strings into a list of lists using map
def strings_to_lists(list_strings):
	return list(map(list, list_strings))


# Task 5. Store each event's start and end dates. Add other verified local events
# here using the same (start_date, end_date) format.
def get_night_of_museums_events(dortmund_events_dict, target_date):
	
	#Fetching the events with the matching date for the night of museums 19.09.2026
	matching_events = [
        event for event, event_date in dortmund_events_dict.items() 
        if event_date == target_date	
    ]
    
	print(f"\nTask5: Events running on Dortmund Nigt of Museums {target_date.strftime('%d/%m/%Y')}:")

	if matching_events:
		for index, event in enumerate(matching_events, start=1):
			print(f"{index}. {event}")
	else:
		print("No events scheduled for this date.")
		
	return matching_events


if __name__ == "__main__":
	#Inputs for task1
	print("\nTask 1:", sort_tuple_last_element(
		[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	))

	#Inputs for task2
	s1 = "Hello 456, I am only 1 test string 4444."
	print("\nTask 2:", sum_and_average_digits(s1))

	#Inputs for task3
	dictionaries = [
		{"make": " Google ", "model": 216, "color": "Black"},
		{"make": "Mi Max", "model": "2", "color": "Gold"},
		{"make": "Samsung", "model": 7, "color": "Blue"},
	]
	print("\nTask 3:", sort_dictionaries_by_color(dictionaries))

	#Input for task4
	list_strings = ["cat", "dog"]
	print("\nTask 4:", strings_to_lists(list_strings))

	#Input for task5
	target_date = date(2026, 9, 19)
	#Dictionary of events in Dortmund from June to December 2026
	dortmund_events_dict = {
		"Juice Jam Festival": date(2026, 6, 13),
		"Bunte Republik Dortmund Street Festival": date(2026, 7, 4),
		"Ruhr Reggae Summer Festival": date(2026, 8, 8),
		"DEW21 Museumsnacht (Night of Museums)": date(2026, 9, 19),
		"Open-Air Concert by Marquess at Friedensplatz": date(2026, 9, 19),
		"Building Projection ('what is wisdom') at Dortmunder U": date(2026, 9, 19),
		"Author Reading by Saša Stanišić at St. Reinoldi": date(2026, 9, 19),
		"Pianist Nicolas Namoradze Concert at Konzerthaus Dortmund": date(2026, 9, 19),
		"Craft Workshops & Exhibitions at Handwerkskammer Dortmund": date(2026, 9, 19),
		"Fiery Show by the FLAMES at Kindermuseum Adlerturm": date(2026, 9, 19),
		"Immersive Stage Performance at Phoenix des Lumières": date(2026, 9, 19),
		"Special Open House & Demos at Fire and Rescue Station 1": date(2026, 9, 19),
		"Dortmunder Herbst Fair": date(2026, 10, 3),
		"Dortmund Christmas Market (Weihnachtsmarkt)": date(2026, 11, 23),
		"Silvester Party at Hansaplatz": date(2026, 12, 31),
		}

	#Call the function to get the events for the night of museums
	matching_events = get_night_of_museums_events(dortmund_events_dict, target_date)
