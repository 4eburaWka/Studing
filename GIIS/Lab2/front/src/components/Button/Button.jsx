

import classes from './Button.module.css'


export default function Button({children, isActive, ...props}) {
    return (
        <>
            <button
                {...props}
                className={
                    isActive ? `${classes.btn_new} ${classes.active}` : classes.btn_new
                }
            > {children} </button>
        </>
    )
}
