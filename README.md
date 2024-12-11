<img width="308" alt="Screenshot 2024-12-11 at 9 52 21 PM" src="https://github.com/user-attachments/assets/9cf9d1dd-f2c9-4484-bc35-5240fbdbf8fa" />

#### Usage

`./brainlet {OPTIONS} text` or `echo text | ./brainlet {OPTIONS}`

#### Options
| Flag               | Description                                         |
| ------------------ | --------------------------------------------------- |
| `-a`, `--align`    | Align text `left`, `right` or `center`              |
| `-s`, `--small`    | Render using smaller glyphs                         |
| `-c`, `--compact`  | Trim empty lines from output                        |
| `-w`, `--width`    | Number of chars until wrap, or zero for no wrapping |
| `-t`, `--tab-size` | Number of spaces to expand tabs to                  |


## Examples

```
╶┬╴╷               ·    ╷     ╷
 │ ├─╮╭─╮   ╭─┐╷ ╷╶╮ ╭─╮│╭╴   ├─╮╭─╮╭─╮╷ ╷┌─╮
 │ │ │├─┘   │ ││ │ │ │  ├┴╮   │ ││  │ │││││ │
 ╵ ╵ ╵╰─╯   ╰─┤╰─┘╶┴╴╰─╯╵ ╰   └─╯╵  ╰─╯╰┴╯╵ ╵
              ╰
 ╭─           ·
╶┼─╭─╮╭┬╮    ╶╮╷ ╷╭┬╮┌─╮╭─╮   ╭─╮╶╮╷╭─╮╭─╮
 │ │ │ │      ││ │││││ │╰─╮   │ │ ││├─┘│
 ╵ ╰─╯╰┴╯     │╰─┘╵ ╵├─╯╰─╯   ╰─╯ ╰╯╰─╯╵
            ╰─╯      ╵
 ╷ ╷        ╶╮               ╷
╶┼╴├─╮╭─╮    │ ╭─╮╶─╮╷ ╷   ╭─┤╭─╮╭─╮
 │ │ │├─┘    │ ╭─┤╭─╯│ │   │ ││ ││ │
 ╰╴╵ ╵╰─╯   ╶┴╴╰─╯╰─╴╰─┤   ╰─┘╰─╯╰─┤ ·
                     ╰─╯         ╰─╯
```

```
╶┬╴╷ ╷╭─╴   ╭─╮╷ ╷╶┬╴╭─╮╷╭╴   ┌╮ ┌─╮╭─╮╷ ╷┌─╮
 │ ├─┤├─    │╶┼│ │ │ │  ├┴╮   ├┴╮├┬╯│ │││││ │
 ╵ ╵ ╵╰─╴   ╰─╯╰─╯╶┴╴╰─╯╵ ╰   └─╯╵╰╴╰─╯╰┴╯╵ ╵
╭─╴╭─╮╭┬╮     ╷╷ ╷╭┬╮┌─╮╭─╮   ╭─╮╶╮╷╭─╴┌─╮
├─╴│ │ │      ││ ││││├─╯╰─╮   │ │ ││├─ ├┬╯
╵  ╰─╯╰┴╯   ╰─╯╰─╯╵ ╵╵  ╰─╯   ╰─╯ ╰╯╰─╴╵╰╴
╶┬╴╷ ╷╭─╴   ╷  ╭─╮╶─╮╷ ╷   ┌─╮╭─╮╭─╮
 │ ├─┤├─    │  ├─┤╭─╯╰┬╯   │ ││ ││╶┐
 ╵ ╵ ╵╰─╴   ╰─╴╵ ╵╰─╴ ╵    └─╯╰─╯╰─╯ ·
```
