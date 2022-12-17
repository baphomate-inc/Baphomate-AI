const pertanyaan = document.getElementById("pertanyaan")
const jawaban = document.getElementById("jawaban")
const loaders = document.getElementById("loaders")
const container = document.getElementsByClassName("container")

let init = 0

const botSay = (data) => {
  return [
    "Perkenalkan saya Baphomate.AI (BETA)ヾ(＾-＾)ノ. siapa nama kamu?",
    `Hallo ${data?.nama}, berapa usia kamu?`,
    `Ohhh ${data?.usia}, hobi kamu apa yaa?`, 
    `wawww hobinya ko sama ${data?.hobi}, btw udah punya pasangan belum?`,
    `ohhh ${data?.pasangan}, ya udah kalau gitu. Apa yang kamu ingin tanyakan?`,
    `Untuk pertanyaan hal " ${data?.tanya} ", Saat ini saya tidak bisa menjawab karna developer yang membuat saya saat ini sedang galau :(`
  ]
}

pertanyaan.innerHTML = botSay()[0]

let usersData = []

function botStart() {
  if (jawaban.value.length < 1) return alert("silahkan isi jawaban dulu")
  init++
  if (init === 1) {
    botDelay({ nama: jawaban.value })
  } else if (init === 2) {
    botDelay({ usia: jawaban.value })
  } else if (init === 3) {
    botDelay({ hobi: jawaban.value })
  } else if (init === 4) {
    botDelay({ pasangan: jawaban.value })
  } else if (init === 5) {
    botDelay({ tanya: jawaban.value })
  }else if (init === 6) {
    finishing()
  } else {
    botEnd()
  }
}

function botDelay(jawabanUser) {
  loaders.style.display = "block"
  container[0].style.filter = "blur(8px)"
  setTimeout(() => {
    pertanyaan.innerHTML = botSay(jawabanUser)[init]
    loaders.style.display = "none"
    container[0].style.filter = "none"
  }, [1000])
  usersData.push(jawaban.value)
  jawaban.value = ""
}

function finishing() {
  pertanyaan.innerHTML = `Thank u yaa ${usersData[0]} udah nyobain Baphomate.AI (BETA) o(〃＾▽＾〃)o, maaf yaa kalo fiturnya masih kurang ಥ_ಥ, kali-kali kita main ${usersData[2]} bareng yaa!`
  jawaban.value = "siap thanks juga!"
}

function botEnd() {
  alert(
    `Terimakasih ${usersData[0]} sudah berkunjung, anda akan diarahkan ke halaman utama.`
  )
  window.location.reload()
}