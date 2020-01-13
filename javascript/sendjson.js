a=function sendJSON(){ 
               
            // Creating a XHR object 
            let xhr = new XMLHttpRequest(); 
            let url = "deployer"; 
        
            // open a connection 
            xhr.open("POST", url, true); 
  
            // Set the request header i.e. which type of content you are sending 
            xhr.setRequestHeader("Content-Type", "application/json"); 
  
            // Create a state change callback 
            xhr.onreadystatechange = function () { 
                if (xhr.readyState === 4 && xhr.status === 200) { 
  
                    // Print received data from server 
                    result.innerHTML = this.responseText; 
  
                } 
            }; 
  
            // Converting JSON data to string 
            var data = JSON.stringify({ "project":{"name":"Profile"},"event_type":"merge_request","object_attributes":{"state":"merged","target_branch":"master"}}); 
  
            // Sending data with the request 
            xhr.send(data); 
        }
