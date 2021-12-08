let imageModelURL = 'https://teachablemachine.withgoogle.com/models/qk2iNZVzO/';

/**** Added by LF */
function selectModel()
{
  let model = document.getElementById("model").value;
  if(model === "glasses")
  {
    document.getElementById("modelOutput").src="glasses.html";
  }
  else
  {
    document.getElementById("modelOutput").src="hood.html";    
  }
  
}