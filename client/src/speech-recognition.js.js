import React,{useState} from 'react'

function Speechrecognition () {
  const [userInput, setUserInput] = useState('');

  const handleInputSubmit = async (event) => {
    event.preventDefault();
    const url = 'http://localhost:5000/execute_jarvis'; // Flask API endpoint URL

    // Make HTTP POST request to Flask API endpoint
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ userInput })
    });

    // Handle response from Flask API endpoint
    const data = await response.json();
    console.log(data);
  };

  return (
    <div>
      <form onSubmit={handleInputSubmit}>
        <input type="text" value={userInput} onChange={(event) => setUserInput(event.target.value)} />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Speechrecognition

