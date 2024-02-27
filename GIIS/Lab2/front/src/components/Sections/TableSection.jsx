import classes from "./sections.module.css"
import {useCallback, useEffect, useState} from "react";
import Button from "../Button/Button.jsx";

export default function TableSection({setActiveTab, setContactId}) {
    const [contactsUrl, setContactsUrl] = useState('http://127.0.0.1:8000/contacts')
    const [contacts, setContacts] = useState({results: []})
    const [search_val, setSearchVal] = useState("")

    const fetchContacts = useCallback(async () => {
        const response = await fetch(contactsUrl)
        const data = await response.json()
        setContacts(data)
    }, [contactsUrl])

    useEffect(() => {
        fetchContacts()
    }, [fetchContacts])

    function handleSearchVal(e) {
        const val = e.target.value
        setSearchVal(val)
    }

    return (
        <section>
            <div className={classes.search_section}>
                <input placeholder="Поиск" id="search" value={search_val} onChange={handleSearchVal}/>
                <button onClick={() => {
                    setContactsUrl(prevState => {
                        if (prevState === null)
                            return
                        let modifiedUrl, index = prevState.indexOf("?search=")
                        if (index !== -1)
                            modifiedUrl = prevState.substring(0, index)
                        else
                            modifiedUrl = prevState
                        return modifiedUrl + `?search=${search_val}`
                    })
                }}>🔍
                </button>
            </div>
            <table className={classes.table_dark}>
                <thead>
                <tr key={9999999999}>
                    <th>id</th>
                    <th>Фамилия</th>
                    <th>Имя</th>
                    <th>Отчество</th>
                    <th>Телефон</th>
                    <th>Адрес</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>

                <tbody>
                {contacts.results.map((contact) => (
                    <tr key={contact.id}>
                        <td>{contact.id}</td>
                        <td>{contact.last_name}</td>
                        <td>{contact.first_name}</td>
                        <td>{contact.surname}</td>
                        <td>{contact.phone}</td>
                        <td>{contact.address}</td>
                        <td><Button children={"✏️"} style={{width: '30px'}} onClick={() => {
                            setActiveTab("edit")
                            setContactId(contact.id)
                        }}/>
                        </td>
                        <td><Button children={"🗑️"} style={{width: '30px', backgroundColor: "red"}} onClick={() => {
                            setActiveTab("delete")
                            setContactId(contact.id)
                        }}/>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>

            <div className={classes.control_buttons}>
                <Button children={"<"} isActive={true} onClick={() => setContactsUrl(contacts.previous)}/>
                <Button children={">"} isActive={true} onClick={() => setContactsUrl(contacts.next)}/>
            </div>
        </section>
    )
}
