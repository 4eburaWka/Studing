import {useState} from 'react'
import './App.css'

import Button from "./components/Button/Button.jsx";
import TableSection from "./components/Sections/TableSection.jsx";
import AddSection from "./components/Sections/AddSection.jsx";
import EditSection from "./components/Sections/EditSection.jsx";
import DeleteSection from "./components/Sections/DeleteSection.jsx";

import {contact2vcard} from "../lib/json2vcf.js";
import axios from "axios";

export default function App() {
    const [tab, setTab] = useState("table")
    const [contactId, setContactId] = useState(0)

    const saveAllContacts = function (e) {
        e.preventDefault()
        axios.get("http://127.0.0.1:8000/get-all-contacts").then((response => {
            if (response.statusText !== "OK")
                alert(response.data)
            else {
                console.log(response.data)
                let data = new Blob([contact2vcard(response.data)], {type: 'text/plain'});
                let url = window.URL.createObjectURL(data);
                let a = document.createElement('a')
                a.href = url
                a.download = 'contacts.vcf'
                document.body.appendChild(a)
                a.click()
                document.body.removeChild(a)
                window.URL.revokeObjectURL(url)
            }
        }))
    }

    return (
        <>
            <div className="buttons">
                <Button children={"Вывод"} isActive={tab === "table"} onClick={() => setTab("table")}/>
                <Button children={"Добавить"} isActive={tab === "add"} onClick={() => setTab("add")}/>
                <Button children={"Экспортировать"} onClick={saveAllContacts}/>
            </div>

            <div className="active_tab">
                {tab === "table" && <TableSection setActiveTab={setTab} setContactId={setContactId}/>}
                {tab === "add" && <AddSection setActiveTab={setTab}/>}
                {tab === "edit" && <EditSection setActiveTab={setTab} contactId={contactId}/>}
                {tab === "delete" && <DeleteSection setActiveTab={setTab} contactId={contactId}/>}
            </div>
        </>
    )
}
