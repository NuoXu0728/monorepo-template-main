**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: Initialize Drawing Window

**Primary Actor**: Application/System

**Goal in Context**: To provide a designated area for users to draw, ensuring it is properly sized and ready for interaction.

**Preconditions**: The application has been started by the user.

**Trigger**: The application's launch or start event.
  
**Scenario 1**: User launches the drawing application.
**Scenario 2**:The application initializes a new window with a specific dimension.
**Scenario 3**:The drawable canvas within the window is set up to be 600 pixels wide by 400 pixels high.
**Scenario 4**:The window is displayed to the user with the canvas ready for drawing.

**Exceptions**: If the display resolution is smaller than the specified canvas size, the window should adjust to fit the screen and inform the user.

**Priority**: High-priority. Without initializing the window and canvas correctly, the primary functionality of drawing will be compromised.

**When available**: First release
**Channel to actor**: Via the GUI interface of the application, specifically the initialized window and canvas.

**Secondary Actor**: User (who interacts with the initialized window)

**Channels to Secondary Actors**: Via the GUI interface of the application, allowing the user to draw and interact with the canvas.

**Open Issues**: How to handle window resizing events by the user?


<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
