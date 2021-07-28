from notes import Collection

# Creates an empty note collection
c = Collection()

# Add a few notes (the C in CRUD)
c.add("Meeting @ 3", "There's a meeting at 3, don't forget!")
c.add("Finish example", "Finish example before tomorrow.")
c.add("Recipe for brownies", "½ cup butter\n1 cup white sugar\n2 eggs\n1 teaspoon vanilla extract\n⅓ cup unsweetened cocoa powder\n½ cup all-purpose flour\n¼ teaspoon salt\n¼ teaspoon baking powder")

# Get a note from an id (the R in CRUD)
n0 = c.get(0)
print(n0)

# Update a note (the U in CRUD)
c.update(n0._id, "Meeting @ 5", "Meeting has been rescheduled to 5.")
print(n0.title + "\n" + n0.content)

# Delete a note (the D in CRUD)
c.delete(c.get(2)._id)
print(c.notes)