import streamlit as st
from love import percent


st.title("2048-style Merging Animation")

# Define the list of numbers
name1 = st.text_input("Enter name of 1st person:", "Minh")
name2 = st.text_input("Enter name of 2nd person:", "Linh")
if name1 and name2:
    d, lst, percent = percent(name1, name2)
    nums = lst[0]

    # Generate the HTML + CSS + JavaScript for the animation
    html_content = f"""
    <div style="display: flex; justify-content: center; gap: 10px; margin-top: 50px;">
    """

    # Add divs for each number
    for idx, num in enumerate(nums):
        html_content += f"""
        <div id="block-{idx}" 
            style="
                width: 50px; 
                height: 50px; 
                background: lightblue; 
                border-radius: 5px; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                font-size: 18px; 
                font-weight: bold;
                transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out;
            ">
            {num}
        </div>
        """

    html_content += "</div>"

    # Add JavaScript for animations
    js_animation = """
    <script>
    function mergeBlocks() {
        let blocks = document.querySelectorAll("div[id^='block-']");
        let n = blocks.length;
        let merged = [];
        
        for (let i = 0; i < Math.ceil(n / 2); i++) {
            let left = blocks[i];
            let right = blocks[n - i - 1];
            let sum = parseInt(left.innerText) + parseInt(right.innerText);
            if (i == n - i - 1){
                sum = parseInt(left.innerText);
            }
            
            // Update left block with the sum
            left.innerText = sum;
            left.style.transform = "scale(1.2)";
            
            // Fade out and hide the right block
            if (left !== right) {
                right.style.opacity = "0";
                setTimeout(() => { right.style.display = "none"; }, 500);
            }
            
            // Add to the merged list
            merged.push(sum);
        }
        
    }
    </script>
    """

    # Add a button to trigger the animation
    html_content += """
    <br>
    <button onclick="mergeBlocks()" 
        style="
            margin-top: 20px; 
            padding: 10px 20px; 
            font-size: 16px; 
            background: #4CAF50; 
            color: white; 
            border: none; 
            border-radius: 5px; 
            cursor: pointer;">
        Start Merging
    </button>
    """

    # Combine everything into the final HTML
    html_content += js_animation

    # Render the HTML in Streamlit
    st.components.v1.html(html_content, height=300)
