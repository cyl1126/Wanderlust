steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE itineraries (

            id SERIAL PRIMARY KEY NOT NULL,
            notes TEXT NOT NULL,
            trip_id INTEGER NOT NULL references trips
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE itineraries;
        """
    ]
]