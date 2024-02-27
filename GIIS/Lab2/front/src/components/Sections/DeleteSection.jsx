import classes from "./sections.module.css";
import axios from "axios";
import {useCallback, useEffect, useState} from "react";


export default function DeleteSection({setActiveTab, contactId}) {
    const [contact, setContact] = useState({})
    const fetchContact = useCallback(async () => {
        const response = await fetch(`http://127.0.0.1:8000/?id=${contactId}`)
        const data = await response.json()
        setContact(data)
    })

    useEffect(() => {
        fetchContact()
    }, [fetchContact])

    const deleteContact = function (e) {
        e.preventDefault()
        axios({
            method: "DELETE",
            url: "http://127.0.0.1:8000/",
            data: {id: contactId}
        }).then(response => {
            response.statusText !== "OK" && alert(response.data) || setActiveTab('table')
        })
    }

    return (
        <section style={{display: "flex", flexDirection: "column"}}>
            <div className={classes.data}>
                <p>
                    {`${contact.last_name} ${contact.first_name} ${contact.surname}`} <br/>
                    {contact.phone} <br/>
                    {contact.address}
                </p>
            </div>

            <div style={{display: "flex", justifyContent: "center"}}>
                <button className={`${classes.btn} ${classes.cancel_btn}`} onClick={() => setActiveTab('table')}>Отмена</button>
                <button className={`${classes.btn} ${classes.del_btn}`} onClick={deleteContact}>Удалить</button>
            </div>
        </section>
    )
}
