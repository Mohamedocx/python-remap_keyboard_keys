import keyboard

# إعادة تعيين زر "A" ليصبح "ذ"
keyboard.remap_key('a', '`')

# إعادة تعيين زر "ذ" ليصبح "A"
keyboard.remap_key('`', 'a')

# جعل البرنامج يعمل باستمرار حتى يتم إيقافه
keyboard.wait('esc')  # اضغط على زر ESC للخروج من البرنامجششش

