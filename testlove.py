import streamlit as st
from love import percent


st.title("Test Your Love :heart: (Don't trust it)")

# Define the list of numbers
name1 = st.text_input("Enter name of 1st person:", "Minh")
name2 = st.text_input("Enter name of 2nd person:", "Linh")


if st.button("Run Animation"):
    d, lst_of_lsts, final_result = percent(name1, name2)

    st.write("### Character Counts")
    st.write(d)

    st.write("### Animation of Merging Process")

    # Pass data to JavaScript
    html_code = f"""
    <div id="grid-container" style="display: grid; grid-template-columns: repeat(10, 50px); gap: 5px; justify-content: center;">
    </div>
    <script>
      const states = {lst_of_lsts}; // Merging steps from Python
      const container = document.getElementById("grid-container");

      function createGrid(numbers) {{
          container.innerHTML = ""; // Clear the grid
          numbers.forEach(num => {{
              const cell = document.createElement("div");
              cell.textContent = num;
              cell.style.width = "50px";
              cell.style.height = "50px";
              cell.style.display = "flex";
              cell.style.alignItems = "center";
              cell.style.justifyContent = "center";
              cell.style.backgroundColor = "#EEE4DA";
              cell.style.borderRadius = "5px";
              cell.style.fontSize = "20px";
              cell.style.fontWeight = "bold";
              cell.style.transition = "transform 0.5s";
              container.appendChild(cell);
          }});
      }}

      async function animateMerging() {{
          for (const state of states) {{
              createGrid(state); // Update grid for each step
              await new Promise(resolve => setTimeout(resolve, 1000)); // Wait 1 second
          }}
      }}

      // Start the animation
      animateMerging();
    </script>
    """
    
    # Embed HTML + JS
    st.components.v1.html(html_code, height=300)

    st.write("### Final Result")
    st.write(f"The final percentage is: **{final_result}%**")
