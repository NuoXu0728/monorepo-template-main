**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Drawing on the Canvas Using Left-Click

**Primary Actor**: User

**Goal in Context**: To draw on the canvas in a continuous manner, emulating the experience of drawing with a pencil on paper.


**Preconditions**: The application is open and running.

**Trigger**: User left-clicks (presses down) on the mouse while hovering over the canvas.
  
**Scenario 1**: User hovers the mouse over the location they intend to start drawing on the canvas.
**Scenario 2**: System recognizes the left mouse button press event
**Scenario 3**:As the user drags the mouse across the canvas, the system continuously changes the pixel color at the current mouse position to the selected color.
**Scenario 4**:User creates a continuous drawing on the canvas by dragging the mouse.
 
**Exceptions**: If the system fails to remember the most recently selected color, the drawing might default to a pre-defined color.

**Priority**: High - This feature is essential for users to create drawings and designs on the canvas.

**When available**: Version 1.0.0 of the application.

**Channel to actor**: Direct interaction through the application's GUI, specifically the canvas area.

**Secondary Actor**: None

**Channels to Secondary Actors**: N/A

**Open Issues**: Handling scenarios where mouse events might be incorrectly detected due to system performance issues.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
