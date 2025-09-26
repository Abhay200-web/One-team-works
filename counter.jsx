import { useState } from "react";


function Counter(){
    const [count,setCount]=useState(0);
    function increment(){
        setCount(count+1)
    }
    useEfffect(()=>console.log("Curent value of count "+count),[count])
    return(
        <>
        <p>{count}</p>
        <button onClick={increment}>Increment</button>
        <button onClick={()=>setCount(count-1)}>Decrement</button>
        </>

    )
}
export default Counter;