export function contact2vcard(contacts) {
    let string = ""
    contacts.forEach(contact => {
        let rows = [];
        rows.push("BEGIN:VCARD");
        rows.push("VERSION:4.0");

        rows.push("N:" + `${contact.last_name} ${contact.first_name} ${contact.surname}`);

        if (contact.phone)
            rows.push("TEL:" + contact.phone)

        if (contact.address) {
            rows.push("ADR;TYPE=home;LABEL=" + `${contact.address}`)
        }

        rows.push("END:VCARD");
        string += rows.join("\n") + "\n\n";
    })
    return string
}