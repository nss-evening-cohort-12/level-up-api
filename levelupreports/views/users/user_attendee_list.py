import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views import Connection

def event_host_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.date,
                e.time,
                e.id as event_id,
                g.title as game_title,
                u.id as user_id,
                u.first_name || " " || u.last_name as user_full_name
            from levelupapi_event e
            join levelupapi_gamerevent eg on e.id = eg.event_id
            join levelupapi_gamer gr on eg.gamer_id = gr.id
            join auth_user u on gr.user_id = u.id
            join levelupapi_game g on e.game_id = g.id

            """)

            dataset = db_cursor.fetchall()
            events_dict = {}

            for row in dataset:
                event = Event()
                event.id = row["event_id"]
                event.date = row['date']
                event.time = row['time']
                event.game_title = row['game_title']

                attendee_dict = {}

                attendee_dict['user_id'] = row['user_id']
                attendee_dict['full_name'] = row['user_full_name']

                if event.id in events_dict:
                    events_dict[event.id]["attendees"].append(attendee_dict)
                else:
                    events_dict[event.id] = {}
                    events_dict[event.id]['date'] = event.date
                    events_dict[event.id]['time'] = event.time
                    events_dict[event.id]['game_title'] = event.game_title
                    events_dict[event.id]['attendees'] = [attendee_dict]

        
        events_list = events_dict.values

        template = 'users/list_with_attendees.html'

        context = {
            'event_attendee_list': events_list
        }

        return render(request, template, context)


