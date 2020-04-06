eel.expose(face_1)
function face_1() {
  console.log("Face 1 Function");
  document.getElementById("face-1").style.display = "block";
  document.getElementById("face-2").style.display = "none";
  document.getElementById("face-3").style.display = "none";
  document.getElementById("face-4").style.display = "none";
  document.getElementById("face-5").style.display = "none";
}

eel.expose(face_2)
function face_2() {
  console.log("Face 2 Function");
  document.getElementById("face-2").style.display = "block";
  document.getElementById("face-1").style.display = "none";
  document.getElementById("face-3").style.display = "none";
  document.getElementById("face-4").style.display = "none";
  document.getElementById("face-5").style.display = "none";
}

eel.expose(face_3)
function face_3() {
  console.log("Face 3 Function");
  document.getElementById("face-3").style.display = "block";
  document.getElementById("face-2").style.display = "none";
  document.getElementById("face-1").style.display = "none";
  document.getElementById("face-4").style.display = "none";
  document.getElementById("face-5").style.display = "none";
}

eel.expose(face_4)
function face_4() {
  console.log("Face 4 Function");
  document.getElementById("face-4").style.display = "block";
  document.getElementById("face-2").style.display = "none";
  document.getElementById("face-3").style.display = "none";
  document.getElementById("face-1").style.display = "none";
  document.getElementById("face-5").style.display = "none";
}

eel.expose(face_5)
function face_5() {
  console.log("Face 5 Function");
  document.getElementById("face-5").style.display = "block";
  document.getElementById("face-2").style.display = "none";
  document.getElementById("face-3").style.display = "none";
  document.getElementById("face-4").style.display = "none";
  document.getElementById("face-1").style.display = "none";
}


