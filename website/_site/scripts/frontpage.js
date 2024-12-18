window.$ = (query, el=document)=>{
    return document.querySelector(query);
};
window.$all = (query, el=document)=>{
    return [...document.querySelectorAll(query)];
};

window.addEventListener("DOMContentLoaded", ()=>{

    document.getElementById("file_upload_form").addEventListener("submit", async (e) => {
        e.preventDefault();

        const form = document.getElementById("file_upload_form");
        const formData = new FormData();
        const file = document.getElementById("file_upload").files[0];
        formData.append("file", file);

        form.style.display = "none";
        document.getElementById("successMessage").style.display = "block";

        document.getElementById("loadingSymbol").style.display = "block";
        
        try {
            const response = await fetch("http://127.0.0.1:8000/new_anim", {
                method: "POST",
                body: formData,
            });


            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
        
            const result = await response.json();
            console.log(result);
        } catch (error) {
            console.error("Error during fetch:", error.message);
        } finally {
            document.getElementById("loadingSymbol").style.display = "none";
        }
        

        document.getElementById("animation_video").src = "/assets/media/videos/animation/480p15/Animation.mp4";
        document.getElementById("video_player").style.display = "block";

        document.getElementById("reset_from_button").style.display = "block";

    })

    document.getElementById("reset_button").addEventListener('click', () => {
        document.getElementById("file_upload_form").reset();

        document.getElementById("successMessage").style.display = "none";


        document.getElementById("video_player").style.display = "none";
        document.getElementById("animation_video").src = "";
        document.getElementById("reset_from_button").style.display = "none";
        document.getElementById("file_upload_form").style.display = "block";

    })
    





});