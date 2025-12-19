import { useState } from "react";
import api from "../api/client";


export default function ChatUI() {
const [msg, setMsg] = useState("");
const [reply, setReply] = useState("");


const send = async () => {
const res = await api.post("/chat", { message: msg });
setReply(res.data.response);
};


return (
<div>
<textarea onChange={e => setMsg(e.target.value)} />
<button onClick={send}>Send</button>
<p>{reply}</p>
</div>
);
}