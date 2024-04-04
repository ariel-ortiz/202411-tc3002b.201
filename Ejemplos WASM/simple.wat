;; Simple examples using webassembly text format

(module

  (func
    (export "meaning_of_life")
    (result i32)

    i32.const 42
  )

  (func
    (export "multiply")
    (param $a i32)
    (param $b i32)
    (result i32)

    local.get $a
    local.get $b
    i32.mul
  )
)
