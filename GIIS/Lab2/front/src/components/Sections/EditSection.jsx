import axios from "axios";

import classes from "./sections.module.css";
import {useCallback, useEffect, useState} from "react";
import Button from "../Button/Button.jsx";

export default function EditSection({setActiveTab, contactId}) {
    const [contact, setContact] = useState({id: contactId})

    const fetchContact = useCallback(async () => {
        const response = await fetch(`http://127.0.0.1:8000/?id=${contactId}`)
        const data = await response.json()
        setContact(data)
    }, [])

    useEffect(() => {
        fetchContact()
    }, [fetchContact])

    const handleInputChange = (e) => {
        const {id, value} = e.target;
        setContact((prevContact) => ({
            ...prevContact,
            [id]: value,
        }));
    };

    const editContact = function (e) {
        e.preventDefault()
        axios.put("http://127.0.0.1:8000", contact).then((response => {
            response.statusText !== "OK" && alert(response.data) || setActiveTab('table')
        }))
    }

    return (
        <form>
            <label htmlFor="last_name">Фамилия</label>
            <input type="text" id="last_name" value={contact.last_name} onChange={handleInputChange}/>
            <label htmlFor="last_name">Имя</label>
            <input type="text" id="first_name" value={contact.first_name} onChange={handleInputChange}/>
            <label htmlFor="last_name">Отчество</label>
            <input type="text" id="surname" value={contact.surname} onChange={handleInputChange}/>
            <label htmlFor="last_name">Телефон</label>
            <input type="text" id="phone" value={contact.phone} onChange={handleInputChange}/>
            <label htmlFor="last_name">Адрес</label>
            <textarea id="address" value={contact.address} onChange={handleInputChange}/>
            <Button children={"Отправить"} isActive={true} onClick={editContact}/>
        </form>
    )
}
