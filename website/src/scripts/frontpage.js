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

        const response = await fetch("http://127.0.0.1:8000/new_anim", {
            method: "POST",
            body: formData,
        });

        form.style.display = "none";
        document.getElementById("successMessage").style.display = "block";

        const result = await response.json();
        console.log(result);

        document.getElementById("animation_video").src = result["video_path"]
        document.getElementById("video_player").style.display = "block";

        document.getElementById("reset_from_button").style.display = "block";

    })

    document.getElementById("reset_button").addEventListener('click', () => {
        document.getElementById("file_upload_form").reset();

        document.getElementById("successMessage").style.display = "none";


        document.getElementById("video_player").style.display = "none";

        document.getElementById("reset_from_button").style.display = "none";
        document.getElementById("file_upload_form").style.display = "block";

    })
    





});