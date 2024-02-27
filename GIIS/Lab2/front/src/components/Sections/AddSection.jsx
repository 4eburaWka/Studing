import classes from "./sections.module.css";
import Button from "../Button/Button.jsx";
import { useCallback, useState } from "react";
import axios from "axios";

export default function AddSection({setActiveTab}) {
    const [contact, setContact] = useState({});

    const addContact = function(e) {
        e.preventDefault()
        axios({
            method: 'post',
            url: "http://127.0.0.1:8000",
            data: contact
        }).then(response => {
            response.statusText !== "OK" && alert(response.data) || setActiveTab('table');
        })
    }

    const handleInputChange = (e) => {
        const { id, value } = e.target;
        setContact(prevContact => ({
            ...prevContact,
            [id]: value,
        }));
    };

    return (
        <form>
            <label htmlFor="last_name">Фамилия</label>
            <input type="text" id="last_name" value={contact.last_name} onChange={handleInputChange} />
            <label htmlFor="first_name">Имя</label>
            <input type="text" id="first_name" value={contact.first_name} onChange={handleInputChange} />
            <label htmlFor="surname">Отчество</label>
            <input type="text" id="surname" value={contact.surname} onChange={handleInputChange} />
            <label htmlFor="phone">Телефон</label>
            <input type="text" id="phone" value={contact.phone} onChange={handleInputChange} />
            <label htmlFor="address">Адрес</label>
            <textarea id="address" value={contact.address} onChange={handleInputChange} />
            <Button children={"Отправить"} isActive={true} onClick={addContact} />
        </form>
    );
}
