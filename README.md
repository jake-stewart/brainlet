```
┌╮ ┌─╮╭─╮╶┬╴┌─╮╷  ╭─╴╶┬╴
├┴╮├┬╯├─┤ │ │ ││  ├─  │ 
└─╯╵╰╴╵ ╵╶┴╴╵ ╵╰─╴╰─╴ ╵ 
```

`brainlet` is similar to `figlet` and `toilet`, but it renders with border chars making it more compact and readable.

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
