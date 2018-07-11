 #!/bin/sh

tpid=`ps aux | grep -c 'testgetpid.jar'`

start(){
#if [ $tpid -le 1 ]; then
#        java -Xms128m -Xmx2048m -jar testgetpid.jar 5 > console.log &
#        echo $! > pid.log
#else
#        echo "alread start. PID:`cat pid.log`"
#        exit 0
#fi
        java -Xms128m -Xmx2048m -jar testgetpid.jar 5 > console.log &
        echo $! > pid.log
}

stop(){
    pid=`cat pid.log`
    echo "Kill pid:$pid"
    kill -15 $pid
    rm pid.log
}

case "$1" in
      start)
           start
            ;;
      stop)
            stop
            ;;
      *)
            echo "unknow command"
            ;;
esac